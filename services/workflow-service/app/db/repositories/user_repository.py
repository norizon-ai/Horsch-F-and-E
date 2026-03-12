"""
User repository for database operations.
"""

from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from app.db.models import User


class UserRepository:
    """Repository for user CRUD operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_external_subject(self, external_subject: str) -> User | None:
        """
        Get user by external subject (identity provider user ID).

        Args:
            external_subject: Identity provider user ID (Azure AD oid, etc.)

        Returns:
            User object if found, None otherwise
        """
        result = await self.db.execute(
            select(User).where(User.external_subject == external_subject)
        )
        return result.scalars().first()

    async def create_user(
        self,
        external_subject: str,
        email: str,
        name: str | None = None
    ) -> User:
        """
        Create a new user.

        Args:
            external_subject: Identity provider user ID
            email: User email address
            name: User's full name (optional)

        Returns:
            Created User object
        """
        user = User(
            external_subject=external_subject,
            email=email,
            name=name,
            last_login=datetime.utcnow()
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update_last_login(self, user: User) -> User:
        """
        Update user's last login timestamp.

        Args:
            user: User object to update

        Returns:
            Updated User object
        """
        user.last_login = datetime.utcnow()
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def upsert_user(
        self,
        external_subject: str,
        email: str,
        name: str | None = None
    ) -> User:
        """
        JIT (Just-In-Time) user provisioning.

        If user exists: Update last_login and return existing user.
        If user doesn't exist: Create new user and return it.

        Args:
            external_subject: Identity provider user ID
            email: User email address
            name: User's full name (optional)

        Returns:
            User object (existing or newly created)
        """
        user = await self.get_by_external_subject(external_subject)

        if user:
            return await self.update_last_login(user)
        else:
            try:
                return await self.create_user(external_subject, email, name)
            except IntegrityError:
                # Race condition: user was created between check and insert
                await self.db.rollback()
                user = await self.get_by_external_subject(external_subject)
                if user:
                    return await self.update_last_login(user)
                else:
                    raise
