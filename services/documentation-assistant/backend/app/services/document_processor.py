"""Document processing service for extracting text from uploaded files"""
from pathlib import Path
from typing import List, Dict
import aiofiles


class DocumentProcessor:
    """Process uploaded documents and extract text content"""

    @staticmethod
    async def process_file(file_path: str) -> Dict[str, str]:
        """
        Extract text from a file

        Args:
            file_path: Path to the file

        Returns:
            Dict with 'filename', 'content', and 'file_type'
        """
        file_path_obj = Path(file_path)
        filename = file_path_obj.name
        file_extension = file_path_obj.suffix.lower()

        try:
            if file_extension in ['.txt', '.md']:
                # Simple text files
                async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = await f.read()
                return {
                    "filename": filename,
                    "content": content,
                    "file_type": file_extension[1:]
                }

            elif file_extension in ['.pdf']:
                # PDF files - would need PyPDF2 or similar
                # For now, return a placeholder
                return {
                    "filename": filename,
                    "content": "[PDF content extraction not yet implemented - install PyPDF2]",
                    "file_type": "pdf"
                }

            elif file_extension in ['.doc', '.docx']:
                # Word documents - would need python-docx
                return {
                    "filename": filename,
                    "content": "[Word document extraction not yet implemented - install python-docx]",
                    "file_type": "docx"
                }

            else:
                return {
                    "filename": filename,
                    "content": f"[Unsupported file type: {file_extension}]",
                    "file_type": "unknown"
                }

        except Exception as e:
            return {
                "filename": filename,
                "content": f"[Error reading file: {str(e)}]",
                "file_type": "error"
            }

    @staticmethod
    async def process_multiple_files(file_paths: List[str]) -> str:
        """
        Process multiple files and combine their content

        Args:
            file_paths: List of file paths

        Returns:
            Combined text content from all files
        """
        combined_content = []

        for file_path in file_paths:
            result = await DocumentProcessor.process_file(file_path)
            combined_content.append(f"## File: {result['filename']}\n\n{result['content']}\n\n")

        return "\n".join(combined_content)
