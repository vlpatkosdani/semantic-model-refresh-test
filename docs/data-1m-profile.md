# Data profile: data-1m-v1

Source: GitHub release `data-1m-v1` of vlpatkosdani/semantic-model-refresh-test (Parquet). Generated with pyarrow from the downloaded files.

| File | Rows | Columns | File size |
|---|---:|---:|---:|
| currencyexchange.parquet | 100,450 | 4 | 0.4 MB |
| customer.parquet | 104,990 | 24 | 7.9 MB |
| date.parquet | 4,018 | 17 | 0.0 MB |
| orderrows.parquet | 2,349,091 | 7 | 28.9 MB |
| orders.parquet | 980,666 | 6 | 7.3 MB |
| product.parquet | 2,517 | 14 | 0.1 MB |
| sales.parquet | 2,349,091 | 13 | 44.0 MB |
| store.parquet | 74 | 11 | 0.0 MB |

Notes:

- `orders` and `orderrows` are a header and detail split of the same rows as `sales`. The models load `sales` only.
- Timestamps are UTC and have no time part. The models drop the zone in `fnLoadParquet`.
- The `data-10m-v1` release has the same file names. Its sales.parquet is 442.7 MB.

## currencyexchange.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| Date | timestamp[ms, tz=UTC] | 4,018 | 0 |
| FromCurrency | string | 5 | 0 |
| ToCurrency | string | 5 | 0 |
| Exchange | decimal128(20, 5) | 31,512 | 0 |

## customer.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| CustomerKey | int32 | 104,990 | 0 |
| GeoAreaKey | int32 | 608 | 0 |
| StartDT | timestamp[ms, tz=UTC] | 11,305 | 0 |
| EndDT | timestamp[ms, tz=UTC] | 14,711 | 0 |
| Continent | string | 3 | 0 |
| Gender | string | 2 | 0 |
| Title | string | 4 | 0 |
| GivenName | string | 9,294 | 0 |
| MiddleInitial | string | 37 | 0 |
| Surname | string | 20,325 | 0 |
| StreetAddress | string | 95,854 | 0 |
| City | string | 34,581 | 0 |
| State | string | 565 | 0 |
| StateFull | string | 610 | 0 |
| ZipCode | string | 40,639 | 0 |
| Country | string | 8 | 0 |
| CountryFull | string | 8 | 0 |
| Birthday | timestamp[ms, tz=UTC] | 24,147 | 0 |
| Age | int32 | 67 | 0 |
| Occupation | string | 2,571 | 0 |
| Company | string | 1,031 | 0 |
| Vehicle | string | 11,760 | 0 |
| Latitude | decimal128(20, 5) | 102,773 | 0 |
| Longitude | decimal128(20, 5) | 103,894 | 0 |

## date.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| Date | timestamp[ms, tz=UTC] | 4,018 | 0 |
| DateKey | string | 4,018 | 0 |
| Year | int32 | 11 | 0 |
| YearQuarter | string | 44 | 0 |
| YearQuarterNumber | int32 | 44 | 0 |
| Quarter | string | 4 | 0 |
| YearMonth | string | 132 | 0 |
| YearMonthShort | string | 132 | 0 |
| YearMonthNumber | int32 | 132 | 0 |
| Month | string | 12 | 0 |
| MonthShort | string | 12 | 0 |
| MonthNumber | int32 | 12 | 0 |
| DayofWeek | string | 7 | 0 |
| DayofWeekShort | string | 7 | 0 |
| DayofWeekNumber | int32 | 7 | 0 |
| WorkingDay | int32 | 2 | 0 |
| WorkingDayNumber | int32 | 2,761 | 0 |

## orderrows.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| OrderKey | int64 | 980,666 | 0 |
| RowNumber | int32 | 7 | 0 |
| ProductKey | int32 | 2,517 | 0 |
| Quantity | int32 | 10 | 0 |
| UnitPrice | decimal128(20, 5) | 1,761 | 0 |
| NetPrice | decimal128(20, 5) | 24,212 | 0 |
| UnitCost | decimal128(20, 5) | 1,956 | 0 |

## orders.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| OrderKey | int64 | 980,666 | 0 |
| CustomerKey | int32 | 86,908 | 0 |
| StoreKey | int32 | 65 | 0 |
| DT | timestamp[ms, tz=UTC] | 3,515 | 0 |
| DeliveryDate | timestamp[ms, tz=UTC] | 3,523 | 0 |
| CurrencyCode | string | 5 | 0 |

## product.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| ProductKey | int32 | 2,517 | 0 |
| ProductCode | string | 2,517 | 0 |
| ProductName | string | 2,517 | 0 |
| Manufacturer | string | 11 | 0 |
| Brand | string | 11 | 0 |
| Color | string | 17 | 0 |
| WeightUnit | string | 4 | 0 |
| Weight | decimal128(20, 5) | 296 | 284 |
| Cost | decimal128(20, 5) | 480 | 0 |
| Price | decimal128(20, 5) | 426 | 0 |
| CategoryKey | int32 | 8 | 0 |
| CategoryName | string | 8 | 0 |
| SubCategoryKey | int32 | 32 | 0 |
| SubCategoryName | string | 32 | 0 |

## sales.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| OrderKey | int64 | 980,666 | 0 |
| LineNumber | int32 | 7 | 0 |
| OrderDate | timestamp[ms, tz=UTC] | 3,515 | 0 |
| DeliveryDate | timestamp[ms, tz=UTC] | 3,523 | 0 |
| CustomerKey | int32 | 86,908 | 0 |
| StoreKey | int32 | 65 | 0 |
| ProductKey | int32 | 2,517 | 0 |
| Quantity | int32 | 10 | 0 |
| UnitPrice | decimal128(20, 5) | 1,761 | 0 |
| NetPrice | decimal128(20, 5) | 24,212 | 0 |
| UnitCost | decimal128(20, 5) | 1,956 | 0 |
| CurrencyCode | string | 5 | 0 |
| ExchangeRate | decimal128(20, 5) | 6,913 | 0 |

## store.parquet

| Column | Parquet type | Distinct | Nulls |
|---|---|---:|---:|
| StoreKey | int32 | 74 | 0 |
| StoreCode | int32 | 67 | 0 |
| GeoAreaKey | int32 | 67 | 0 |
| CountryCode | string | 9 | 0 |
| CountryName | string | 9 | 0 |
| State | string | 67 | 0 |
| OpenDate | timestamp[ms, tz=UTC] | 32 | 0 |
| CloseDate | timestamp[ms, tz=UTC] | 15 | 58 |
| Description | string | 67 | 0 |
| SquareMeters | int32 | 39 | 1 |
| Status | string | 3 | 1 |
