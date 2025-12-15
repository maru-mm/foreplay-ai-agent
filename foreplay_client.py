"""
Foreplay API Client - Complete Integration
Author: Wasa
Description: Complete Python client for all Foreplay API endpoints
"""

import requests
from typing import Optional, Dict, Any, List
from urllib.parse import urljoin
import json


class ForeplayAPIClient:
    """
    Complete Foreplay API Client with all available endpoints.
    
    Base URL: https://public.api.foreplay.co/
    Documentation: https://docs.foreplay.co/
    """
    
    BASE_URL = "https://public.api.foreplay.co/"
    
    def __init__(self, api_key: str):
        """
        Initialize the Foreplay API client.
        
        Args:
            api_key: Your Foreplay API key from the dashboard
        """
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the Foreplay API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            data: Request body data
            
        Returns:
            JSON response from the API
            
        Raises:
            requests.exceptions.RequestException: If the request fails
        """
        url = urljoin(self.BASE_URL, endpoint)
        
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=data
        )
        
        # Check for API credits remaining
        if 'X-Credits-Remaining' in response.headers:
            print(f"Credits Remaining: {response.headers['X-Credits-Remaining']}")
        
        response.raise_for_status()
        return response.json()
    
    # =============================================================================
    # SWIPEFILE ENDPOINTS
    # =============================================================================
    
    def get_swipefile_ads(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        live: Optional[bool] = None,
        display_format: Optional[str] = None,
        publisher_platform: Optional[str] = None,
        niche: Optional[str] = None,
        market_target: Optional[str] = None,
        language: Optional[str] = None,
        search: Optional[str] = None,
        offset: int = 0,
        limit: int = 10,
        order: str = "newest"
    ) -> Dict[str, Any]:
        """
        Retrieve ads from your personal swipefile collection.
        
        Args:
            start_date: Filter ads published after this date (YYYY-MM-DD)
            end_date: Filter ads published before this date (YYYY-MM-DD)
            live: Filter by ad status (active/inactive)
            display_format: Filter by ad format (video, image, carousel, etc.)
            publisher_platform: Filter by platform (Facebook, Instagram, etc.)
            niche: Filter by industry/category
            market_target: Filter by target audience (B2B, B2C)
            language: Filter by ad language
            search: Search query string
            offset: Number of results to skip (default 0)
            limit: Results per page (default 10)
            order: Sort order (newest, oldest, longest_running, most_relevant, saved_newest)
            
        Returns:
            Dictionary containing ads and metadata
        """
        params = {
            "offset": offset,
            "limit": limit,
            "order": order
        }
        
        # Add optional filters
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if live is not None:
            params["live"] = live
        if display_format:
            params["display_format"] = display_format
        if publisher_platform:
            params["publisher_platform"] = publisher_platform
        if niche:
            params["niche"] = niche
        if market_target:
            params["market_target"] = market_target
        if language:
            params["language"] = language
        if search:
            params["search"] = search
        
        return self._make_request("GET", "api/swipefile/ads", params=params)
    
    # =============================================================================
    # BOARDS ENDPOINTS
    # =============================================================================
    
    def get_boards(self) -> Dict[str, Any]:
        """
        Get all your boards.
        
        Note: This endpoint returns all boards without pagination parameters.
        
        Returns:
            Dictionary containing boards list
        """
        return self._make_request("GET", "api/boards")
    
    def get_board_brands(
        self,
        board_id: str,
        offset: int = 0,
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Get brands from a specific board.
        
        Args:
            board_id: The ID of the board
            offset: Number of results to skip
            limit: Results per page
            
        Returns:
            Dictionary containing brands in the board
        """
        params = {
            "board_id": board_id,
            "offset": offset,
            "limit": limit
        }
        return self._make_request("GET", "api/board/brands", params=params)
    
    def get_board_ads(
        self,
        board_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        live: Optional[bool] = None,
        display_format: Optional[str] = None,
        publisher_platform: Optional[str] = None,
        search: Optional[str] = None,
        offset: int = 0,
        limit: int = 10,
        order: str = "newest"
    ) -> Dict[str, Any]:
        """
        Get ads from a specific board.
        
        Args:
            board_id: The ID of the board
            start_date: Filter ads published after this date
            end_date: Filter ads published before this date
            live: Filter by ad status
            display_format: Filter by ad format
            publisher_platform: Filter by platform
            search: Search query string
            offset: Number of results to skip
            limit: Results per page
            order: Sort order
            
        Returns:
            Dictionary containing ads from the board
        """
        params = {
            "board_id": board_id,
            "offset": offset,
            "limit": limit,
            "order": order
        }
        
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if live is not None:
            params["live"] = live
        if display_format:
            params["display_format"] = display_format
        if publisher_platform:
            params["publisher_platform"] = publisher_platform
        if search:
            params["search"] = search
        
        return self._make_request("GET", "api/board/ads", params=params)
    
    # =============================================================================
    # SPYDER ENDPOINTS
    # =============================================================================
    
    def get_spyder_brands(
        self,
        offset: int = 0,
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Get brands from Spyder (competitive intelligence tool).
        
        Args:
            offset: Number of results to skip
            limit: Results per page
            
        Returns:
            Dictionary containing Spyder brands
        """
        params = {
            "offset": offset,
            "limit": limit
        }
        return self._make_request("GET", "api/spyder/brands", params=params)
    
    def get_spyder_brand(
        self,
        brand_id: str
    ) -> Dict[str, Any]:
        """
        Get details for a specific Spyder brand.
        
        Args:
            brand_id: The ID of the brand
            
        Returns:
            Dictionary containing brand details
        """
        params = {
            "brand_id": brand_id
        }
        return self._make_request("GET", "api/spyder/brand", params=params)
    
    def get_spyder_brand_ads(
        self,
        brand_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        live: Optional[bool] = None,
        display_format: Optional[str] = None,
        publisher_platform: Optional[str] = None,
        niches: Optional[str] = None,
        market_target: Optional[str] = None,
        languages: Optional[str] = None,
        offset: int = 0,
        limit: int = 10,
        order: str = "newest"
    ) -> Dict[str, Any]:
        """
        Get ads from a specific Spyder brand.
        
        Args:
            brand_id: The ID of the brand
            start_date: Filter ads published after this date
            end_date: Filter ads published before this date
            live: Filter by ad status
            display_format: Filter by ad format
            publisher_platform: Filter by platform
            niches: Filter by niche
            market_target: Filter by B2B/B2C
            languages: Filter by language
            offset: Number of results to skip
            limit: Results per page
            order: Sort order
            
        Returns:
            Dictionary containing ads from the Spyder brand
        """
        params = {
            "brand_id": brand_id,
            "offset": offset,
            "limit": limit,
            "order": order
        }
        
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if live is not None:
            params["live"] = live
        if display_format:
            params["display_format"] = display_format
        if publisher_platform:
            params["publisher_platform"] = publisher_platform
        if niches:
            params["niches"] = niches
        if market_target:
            params["market_target"] = market_target
        if languages:
            params["languages"] = languages
        
        return self._make_request("GET", "api/spyder/brand/ads", params=params)
    
    # =============================================================================
    # ADS ENDPOINTS
    # =============================================================================
    
    def get_ad(self, ad_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific ad by ID (query parameter version).
        
        Args:
            ad_id: The ID of the ad
            
        Returns:
            Dictionary containing ad details
        """
        params = {"ad_id": ad_id}
        return self._make_request("GET", "api/ad", params=params)
    
    def get_ad_by_id(self, ad_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific ad by ID (path parameter version).
        
        Args:
            ad_id: The ID of the ad
            
        Returns:
            Dictionary containing ad details
        """
        return self._make_request("GET", f"api/ad/{ad_id}")
    
    # =============================================================================
    # BRANDS ENDPOINTS
    # =============================================================================
    
    def get_ads_by_brand_id(
        self,
        brand_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        live: Optional[bool] = None,
        display_format: Optional[str] = None,
        publisher_platform: Optional[str] = None,
        niches: Optional[str] = None,
        market_target: Optional[str] = None,
        languages: Optional[str] = None,
        offset: int = 0,
        limit: int = 10,
        order: str = "newest"
    ) -> Dict[str, Any]:
        """
        Get ads by brand ID.
        
        Args:
            brand_id: The ID of the brand (or multiple comma-separated IDs)
            start_date: Filter ads published after this date
            end_date: Filter ads published before this date
            live: Filter by ad status
            display_format: Filter by ad format (video, carousel, image, dco, dpa, etc.)
            publisher_platform: Filter by platform (Facebook, Instagram, Messenger, Audience Network)
            niches: Filter by niche
            market_target: Filter by B2B/B2C
            languages: Filter by language
            offset: Number of results to skip
            limit: Results per page
            order: Sort order (newest, oldest, longest_running, most_relevant)
            
        Returns:
            Dictionary containing ads from the brand
        """
        params = {
            "brand_id": brand_id,
            "offset": offset,
            "limit": limit,
            "order": order
        }
        
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if live is not None:
            params["live"] = live
        if display_format:
            params["display_format"] = display_format
        if publisher_platform:
            params["publisher_platform"] = publisher_platform
        if niches:
            params["niches"] = niches
        if market_target:
            params["market_target"] = market_target
        if languages:
            params["languages"] = languages
        
        return self._make_request("GET", "api/brand/getAdsByBrandId", params=params)
    
    def get_ads_by_page_id(
        self,
        page_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        live: Optional[bool] = None,
        display_format: Optional[str] = None,
        publisher_platform: Optional[str] = None,
        niches: Optional[str] = None,
        market_target: Optional[str] = None,
        languages: Optional[str] = None,
        offset: int = 0,
        limit: int = 10,
        order: str = "newest"
    ) -> Dict[str, Any]:
        """
        Get ads by Facebook/Instagram page ID.
        
        Args:
            page_id: The Facebook/Instagram page ID
            start_date: Filter ads published after this date
            end_date: Filter ads published before this date
            live: Filter by ad status
            display_format: Filter by ad format
            publisher_platform: Filter by platform
            niches: Filter by niche
            market_target: Filter by B2B/B2C
            languages: Filter by language
            offset: Number of results to skip
            limit: Results per page
            order: Sort order
            
        Returns:
            Dictionary containing ads from the page
        """
        params = {
            "page_id": page_id,
            "offset": offset,
            "limit": limit,
            "order": order
        }
        
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if live is not None:
            params["live"] = live
        if display_format:
            params["display_format"] = display_format
        if publisher_platform:
            params["publisher_platform"] = publisher_platform
        if niches:
            params["niches"] = niches
        if market_target:
            params["market_target"] = market_target
        if languages:
            params["languages"] = languages
        
        return self._make_request("GET", "api/brand/getAdsByPageId", params=params)
    
    def get_brands_by_domain(
        self,
        domain: str,
        offset: int = 0,
        limit: int = 10,
        order: str = "most_ranked"
    ) -> Dict[str, Any]:
        """
        Get brands by domain name.
        
        Args:
            domain: The domain name (e.g., "example.com", "https://example.com", or subdomain)
            offset: Number of results to skip
            limit: Results per page (default 10)
            order: Sort order ('most_ranked' or 'least_ranked')
            
        Returns:
            Dictionary containing brands matching the domain
        """
        params = {
            "domain": domain,
            "offset": offset,
            "limit": limit,
            "order": order
        }
        return self._make_request("GET", "api/brand/getBrandsByDomain", params=params)
    
    def get_brand_analytics(
        self,
        id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        order: str = "newest"
    ) -> Dict[str, Any]:
        """
        Get analytics for a specific brand or page.
        
        Args:
            id: The brand ID (20-25 chars) or Facebook page ID
            start_date: Start date for analytics period (max 30 days range)
            end_date: End date for analytics period
            order: Sort order (newest or oldest)
            
        Returns:
            Dictionary containing brand analytics data (running ads distribution, creative velocity)
        """
        params = {
            "id": id,
            "order": order
        }
        
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        
        return self._make_request("GET", "api/brand/analytics", params=params)
    
    # =============================================================================
    # DISCOVERY ENDPOINTS
    # =============================================================================
    
    def discover_ads(
        self,
        query: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        live: Optional[bool] = None,
        display_format: Optional[str] = None,
        publisher_platform: Optional[str] = None,
        niches: Optional[str] = None,
        market_target: Optional[str] = None,
        languages: Optional[str] = None,
        offset: int = 0,
        limit: int = 10,
        order: str = "newest"
    ) -> Dict[str, Any]:
        """
        Discover new ads from the entire Foreplay database.
        
        Args:
            query: Search query string (free-text search on ad names/descriptions)
            start_date: Filter ads published after this date
            end_date: Filter ads published before this date
            live: Filter by ad status
            display_format: Filter by ad format
            publisher_platform: Filter by platform
            niches: Filter by industry/category
            market_target: Filter by target audience (b2b or b2c)
            languages: Filter by ad language
            offset: Number of results to skip
            limit: Results per page
            order: Sort order (newest, oldest, longest_running, most_relevant)
            
        Returns:
            Dictionary containing discovered ads
        """
        params = {
            "offset": offset,
            "limit": limit,
            "order": order
        }
        
        if query:
            params["query"] = query
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if live is not None:
            params["live"] = live
        if display_format:
            params["display_format"] = display_format
        if publisher_platform:
            params["publisher_platform"] = publisher_platform
        if niches:
            params["niches"] = niches
        if market_target:
            params["market_target"] = market_target
        if languages:
            params["languages"] = languages
        
        return self._make_request("GET", "api/discovery/ads", params=params)
    
    def discover_brands(
        self,
        query: Optional[str] = None,
        offset: int = 0,
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Discover brands from the Foreplay database.
        
        Args:
            query: Search query string (fuzzy matching on brand names)
            offset: Number of results to skip
            limit: Results per page
            
        Returns:
            Dictionary containing discovered brands with details
        """
        params = {
            "offset": offset,
            "limit": limit
        }
        
        if query:
            params["query"] = query
        
        return self._make_request("GET", "api/discovery/brands", params=params)
    
    # =============================================================================
    # USAGE ENDPOINT
    # =============================================================================
    
    def get_usage(self) -> Dict[str, Any]:
        """
        Get your API usage statistics and remaining credits.
        This endpoint does not consume any credits.
        
        Returns:
            Dictionary containing usage statistics
        """
        return self._make_request("GET", "api/usage")

