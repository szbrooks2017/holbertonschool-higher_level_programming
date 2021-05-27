-- convert to utf8.
ALTER DATABASE htbn_0c_0 CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE htbn_0c_0.first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE htbn_0c_0.first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_chi;
