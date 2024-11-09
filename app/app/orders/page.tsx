'use client';

import OrderList from '@/components/orders/OrderLIst';
import { Order } from '@/types/order';
import api from '@/utils/axios';
import { useEffect, useState } from 'react';

const OrdersPage = () => {
  const [orders, setOrders] = useState<Array<Order>>([]);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await api.get('/orders');
        setOrders(response.data.results);
      } catch (error) {
        console.error('Failed to fetch orders:', error);
      }
    };

    fetchOrders();
  }, []);

  return (
    <div className="flex flex-col">
      <OrderList orders={orders} />
    </div>
  );
};

export default OrdersPage;
