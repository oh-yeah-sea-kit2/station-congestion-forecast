CREATE TABLE posts (
  url varchar(1024) UNIQUE NOT NULL,
  time varchar(1024) NOT NULL,
  title varchar(1024) NOT NULL,
  -- date varchar(1024) NOT NULL,
  date_start TIMESTAMP NOT NULL,
  date_end TIMESTAMP NOT NULL
)