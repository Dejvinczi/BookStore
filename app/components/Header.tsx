import Link from 'next/link';
import Navigation from '@components/Navigation';

export default function Header() {
  return (
    <header className='bg-gray-800 py-4 text-white'>
      <div className='container mx-auto flex items-center justify-between px-4'>
        <Link href='/'>
          <h1 className='text-2xl font-bold'>BookStore</h1>
        </Link>
        <Navigation />
      </div>
    </header>
  );
}
