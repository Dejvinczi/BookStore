import { Order } from '@/types/order';
import OrderCard from './OrderCard';

interface OrderListProps {
  orders: Array<Order>;
}

const OrderList = ({ orders }: OrderListProps) => {
  return (
    <div className="p-6">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {orders.map((order) => (
          <OrderCard key={order.id} order={order} />
        ))}
      </div>
    </div>
  );
};

export default OrderList;
