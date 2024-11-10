

with base as (

    select * from {{ref('orders_00_base')}}

),

final as (

    select
        date(o_orderdate) as order_date,
        o_orderpriority as order_priority,
        sum(o_totalprice) as sum_amount
    from base
    group by 1,2

)

select * from final
