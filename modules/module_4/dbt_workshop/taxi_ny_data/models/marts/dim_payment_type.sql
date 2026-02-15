with trips_unioned as (
    select * from {{ ref('int_trips_unioned') }}
),

payment_types as (
    select
        distinct payment_type,
        {{ get_payment_description('payment_type') }} as payment_type_description
    from trips_unioned
)
select *
from payment_types