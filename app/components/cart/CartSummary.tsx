"use client";

import { Button } from "@/components/shared/Button";
import { Input } from "@/components/shared/Input";
import api from "@/utils/axios";
import { useRouter } from "next/navigation";
import { useState } from "react";

interface CartSummaryProps {
  totalPrice: number;
  isEmptyCart: boolean;
}

export const CartSummary: React.FC<CartSummaryProps> = ({
  totalPrice,
  isEmptyCart,
}) => {
  const [address, setAddress] = useState("");
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      await api.post("/orders", {
        address,
      });

      router.push("/orders");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className='flex flex-col gap-4'>
      <Input
        label='Address'
        className='w-full px-3 py-2 rounded-md bg-secondary placeholder-grey-400 focus:ring-4 focus:ring-accent'
        type='text'
        id='address'
        value={address}
        onChange={(e) => setAddress(e.target.value)}
        disabled={isEmptyCart}
      />
      <div className='flex justify-between items-center'>
        <span className='text-lg font-bold text-light'>
          Total: {totalPrice}
        </span>
        <Button
          type='submit'
          className='font-bold py-2 px-4 rounded-lg transition duration-300'
          disabled={isEmptyCart}
        >
          Submit Order
        </Button>
      </div>
    </form>
  );
};
