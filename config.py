"""
Configuration module for Foreplay API Client
"""

import os
from typing import Optional


class ForeplayConfig:
    """Configuration class for Foreplay API"""
    
    # API Settings
    API_KEY: Optional[str] = os.getenv("FOREPLAY_API_KEY")
    BASE_URL: str = os.getenv("FOREPLAY_BASE_URL", "https://public.api.foreplay.co/")
    
    # Default Parameters
    DEFAULT_LIMIT: int = 10
    DEFAULT_OFFSET: int = 0
    DEFAULT_ORDER: str = "newest"
    
    # Request Settings
    REQUEST_TIMEOUT: int = 30  # seconds
    MAX_RETRIES: int = 3
    
    # Display Formats
    DISPLAY_FORMATS = [
        "video",
        "image",
        "carousel",
        "collection"
    ]
    
    # Publisher Platforms
    PUBLISHER_PLATFORMS = [
        "Facebook",
        "Instagram",
        "Messenger",
        "Audience Network"
    ]
    
    # Market Targets
    MARKET_TARGETS = [
        "B2C",  # Business to Consumer
        "B2B"   # Business to Business
    ]
    
    # Sort Orders
    SORT_ORDERS = [
        "newest",
        "oldest",
        "longest_running",
        "most_relevant",
        "saved_newest"  # SwipeFile only
    ]
    
    # Popular Niches (examples)
    NICHES = [
        "Health & Fitness",
        "Food & Beverage",
        "Fashion",
        "Beauty",
        "Technology",
        "Finance",
        "Education",
        "Travel",
        "Entertainment",
        "Real Estate",
        "E-commerce",
        "SaaS",
        "Gaming"
    ]
    
    @classmethod
    def validate_api_key(cls) -> bool:
        """Check if API key is configured"""
        return cls.API_KEY is not None and cls.API_KEY != ""
    
    @classmethod
    def get_api_key(cls) -> str:
        """Get API key or raise error"""
        if not cls.validate_api_key():
            raise ValueError(
                "API key not configured. Set FOREPLAY_API_KEY environment variable "
                "or update config.py"
            )
        return cls.API_KEY


# Singleton instance
config = ForeplayConfig()

