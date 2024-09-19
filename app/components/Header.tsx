import Image from "next/image";
import Link from "next/link";
import Navigation from "@components/Navigation";

export default function Header() {
  return (
    <header className='py-4'>
      <div className='container mx-auto flex items-center justify-between px-4'>
        <Link className='flex items-center' href='/'>
          <Image
            src='/android-chrome-512x512.png'
            alt='Logo'
            width={36}
            height={36}
            className='mr-2'
          />
          <h1 className='text-2xl font-bold'>BookStore</h1>
        </Link>
        <Navigation />
      </div>
    </header>
  );
}
