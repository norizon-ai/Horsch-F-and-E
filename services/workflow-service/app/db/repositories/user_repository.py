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

    async def get_by_auth0_subject(self, auth0_subject: str) -> User | None:
        """
        Get user by Auth0 subject (user ID).

        Args:
            auth0_subject: Auth0 user ID (e.g., "auth0|abc123")

        Returns:
            User object if found, None otherwise
        """
        result = await self.db.execute(
            select(User).where(User.auth0_subject == auth0_subject)
        )
        return result.scalars().first()

    async def create_user(
        self,
        auth0_subject: str,
        email: str,
        name: str | None = None
    ) -> User:
        """
        Create a new user.

        Args:
            auth0_subject: Auth0 user ID
            email: User email address
            name: User's full name (optional)

        Returns:
            Created User object
        """
        user = User(
            auth0_subject=auth0_subject,
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
        auth0_subject: str,
        email: str,
        name: str | None = None
    ) -> User:
        """
        JIT (Just-In-Time) user provisioning.

        If user exists: Update last_login and return existing user.
        If user doesn't exist: Create new user and return it.

        Args:
            auth0_subject: Auth0 user ID
            email: User email address
            name: User's full name (optional)

        Returns:
            User object (existing or newly created)
        """
        # Check if user exists
        user = await self.get_by_auth0_subject(auth0_subject)

        if user:
            # User exists - update last_login
            return await self.update_last_login(user)
        else:
            # User doesn't exist - create new user
            try:
                return await self.create_user(auth0_subject, email, name)
            except IntegrityError:
                # Race condition: user was created between check and insert
                # Rollback and fetch the existing user
                await self.db.rollback()
                user = await self.get_by_auth0_subject(auth0_subject)
                if user:
                    return await self.update_last_login(user)
                else:
                    # This shouldn't happen, but raise if it does
                    raise
