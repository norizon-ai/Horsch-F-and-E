"""
Data models for the Intranet Connector.

Contains data structures for articles and communication,
not configuration (which is in the config folder).
"""

from models.articles import RawArticle, RawArticleSource, RawArticleAuthor
from models.communication import CrawlJob

__all__ = [
    'RawArticle',
    'RawArticleSource', 
    'RawArticleAuthor',
    'CrawlJob'
]