import { Order } from '@/types/order';

interface OrderCardProps {
  order: Order;
}

const OrderCard = ({ order }: OrderCardProps) => {
  return (
    <div className="p-6 rounded-xl bg-primary">
      <div className="flex flex-col gap-1">
        <div className="flex items-center gap-2">
          <span className="text-accent">Order</span>
          <span className="text-accent">#{order.no}</span>
        </div>
        <span className="text-gray-400 text-sm mb-1">{order.address}</span>
      </div>

      <div className="flex justify-between mt-2">
        <div>
          <span className="text-accent text-xl">{order.totalPrice}</span>
        </div>
        <div className="bg-white/10 text-white px-4 py-1.5 rounded-full text-sm flex items-center gap-2">
          <span className="w-2 h-2 bg-white rounded-full"></span>
          <span>{order.status}</span>
        </div>
      </div>
    </div>
  );
};

export default OrderCard;
