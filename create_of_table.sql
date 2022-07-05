create table clients(
		clnt_id serial primary key,
		name VARCHAR(255),
		short_name VARCHAR(100),
		address VARCHAR(500),
		jur_type INT not null);

create table banks(
		bank_id serial primary key,
		name VARCHAR(255) not null,
		bik INT not null);

create table contributions(
		clnt_clnt_id INT not null,
		bank_bank_id INT not null,
		date_open DATE not null,
		date_close DATE,
		date_update DATE,
		procent INT not null,
		month_contrib INT not null,
		primary key (clnt_clnt_id, bank_bank_id),
		foreign key (clnt_clnt_id)
			references clients (clnt_id),
		foreign key (bank_bank_id)
			references banks (bank_id));