-- Guild Table
CREATE TABLE public.guilds
(
    id bigint NOT NULL,
    CONSTRAINT guild_id PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.guilds
    OWNER to postgres;

-- League Table
CREATE TABLE public.leagues
(
    id uuid NOT NULL,
    guild_id bigint NOT NULL,
    owner_id bigint NOT NULL,
    name character varying(25)[] NOT NULL,
    description character varying(150)[] NOT NULL DEFAULT '{}'::character varying[],
    start_date date NOT NULL,
    end_date date NOT NULL,
    can_join_late boolean NOT NULL DEFAULT false,
    is_public boolean NOT NULL DEFAULT true,
    players bigint[] NOT NULL DEFAULT '{}'::bigint[],
    invites bigint[] NOT NULL DEFAULT '{}'::bigint[],
    are_portfolios_public boolean NOT NULL DEFAULT true,
    has_limit_orders boolean NOT NULL DEFAULT false,
    has_short_selling boolean NOT NULL DEFAULT false,
    has_margin_selling boolean NOT NULL DEFAULT false,
    has_stop_loss boolean NOT NULL DEFAULT false,
    has_partial_shares boolean NOT NULL DEFAULT false,
    start_balance integer NOT NULL DEFAULT 10000000,
    commission_value integer NOT NULL DEFAULT 1000,
    min_price integer NOT NULL DEFAULT 200,
    max_price integer NOT NULL DEFAULT 50000000,
    CONSTRAINT league_id PRIMARY KEY (id),
    CONSTRAINT guild_id FOREIGN KEY (guild_id)
        REFERENCES public.guilds (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public.leagues
    OWNER to postgres;

-- Player Table
CREATE TABLE public.players
(
    id uuid NOT NULL,
    league_id uuid NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT player_id PRIMARY KEY (id),
    CONSTRAINT league_id FOREIGN KEY (league_id)
        REFERENCES public.leagues (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public.players
    OWNER to postgres;