with final as (

    select * from {{ref('orders_10_transform')}}

)

select * from final