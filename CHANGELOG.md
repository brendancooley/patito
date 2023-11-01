## v0.7.1 (2023-11-01)

### Fix

- **commitizen**: using `pep440` instead of `semVer`

## v0.7.0 (2023-11-01)

### Fix

- better nested dtype discovery (#9)
- optional nested models are ok (#5)

## v0.6.2 (2023-10-31)

### Fix

- update LDF.collect() for polars==0.19.8
- switch to *args/**kwargs
- `DataFrameValidationError` mirrors pydantic v1 `ValidationError`

## v0.6.1 (2023-10-21)

### Fix

- **v2**: `schema()` - `model_schema_json()`

## v0.6.0 (2023-10-21)

### Fix

- **pydantic**: moved in v2
- **BaseModel**: Changes to pydantic.BaseModel v1 -> v2
- **BP001: `pydatic` v1 -> v2**: Add default None to Optional[T] fields.
- update LDF.collect() for polars==0.19.8
- switch to *args/**kwargs
