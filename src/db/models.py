"""
File: models.py
Author: Andrew Silkwood
Date Created: 2025-02-17
Description:
    Holds models for database tables. If project scale grows too large, this
    will become a folder of model files.
"""

from datetime import date
from uuid import UUID


class Guild:
    def __init__(self, id: int):
        self.id = id

    @classmethod
    def from_row(cls, row):
        return cls(id=row["id"])

    def __repr__(self):
        return f"<Guild(id={self.id})>"


class League:
    def __init__(
        self,
        id: UUID,
        guild_id: int,
        owner_id: int,
        name: str,
        description: str,
        start_date: date,
        end_date: date,
        can_join_late: bool,
        is_public: bool,
        players: list[int],
        invites: list[int],
        are_portfolios_public: bool,
        has_limit_orders: bool,
        has_short_selling: bool,
        has_margin_selling: bool,
        has_stop_loss: bool,
        has_partial_shares: bool,
        start_balance: int,
        commision_value: int,
        min_price: int,
        max_price: int,
    ):
        self.id = id
        self.guild_id = guild_id
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.can_join_late = can_join_late
        self.is_public = is_public
        self.players = players
        self.invites = invites
        self.are_portfolios_public = are_portfolios_public
        self.has_limit_orders = has_limit_orders
        self.has_short_selling = has_short_selling
        self.has_margin_selling = has_margin_selling
        self.has_stop_loss = has_stop_loss
        self.has_partial_shares = has_partial_shares
        self.start_balance = start_balance
        self.commision_value = commision_value
        self.min_price = min_price
        self.max_price = max_price

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            guild_id=row["guild_id"],
            owner_id=row["owner_id"],
            name=row["name"],
            description=row["description"],
            start_date=row["start_date"],
            end_date=row["end_date"],
            can_join_late=row["can_join_late"],
            is_public=row["is_public"],
            players=row["players"],
            invites=row["invites"],
            are_portfolios_public=row["are_portfolios_public"],
            has_limit_orders=row["has_limit_orders"],
            has_short_selling=row["has_short_selling"],
            has_margin_selling=row["has_margin_selling"],
            has_stop_loss=row["has_stop_loss"],
            has_partial_shares=row["has_partial_shares"],
            start_balance=row["start_balance"],
            commision_value=row["commision_value"],
            min_price=row["min_price"],
            max_price=row["max_price"],
        )

    def __repr__(self):
        return f"<League(id={self.id}, owner_id={self.user_id}, name={self.name})>"


class Player:
    def __init__(self, id: UUID, league_id: UUID, user_id: int):
        self.id = id
        self.league_id = league_id
        self.user_id = user_id

    @classmethod
    def from_row(cls, row):
        return cls(id=row["id"], league_id=row["league_id"], user_id=row["user_id"])

    def __repr__(self):
        return f"<Player(id={self.id}, league_id={self.league_id}, user_id={self.user_id})>"
