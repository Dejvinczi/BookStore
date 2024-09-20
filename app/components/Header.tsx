import Image from "next/image";
import Link from "next/link";

export default function Header() {
  return (
    <header className='py-4 px-4 bg-cream-50 shadow-md'>
      <div className='grid grid-cols-3 md:grid-cols-3 items-center'>
        <Link href='/' className='flex items-center'>
          <Image
            src='/android-chrome-192x192.png'
            alt='Logo'
            width={26}
            height={26}
            className='mr-2'
          />
          <h1 className='text-2xl font-bold text-azure-700'>BookStore</h1>
        </Link>

        <nav className='flex-grow flex space-x-8 justify-center'>
          <Link
            href='/books'
            className='text-lg text-stone-600 hover:text-azure-500 transition duration-300'
          >
            Books
          </Link>
          <Link
            href='/authors'
            className='text-lg text-stone-600 hover:text-azure-500 transition duration-300'
          >
            Authors
          </Link>
          <Link
            href='/genres'
            className='text-lg text-stone-600 hover:text-azure-500 transition duration-300'
          >
            Genres
          </Link>
        </nav>

        <div className='flex items-center space-x-4 justify-end'>
          <button className='bg-azure-500 hover:bg-azure-700 text-white font-bold py-2 px-4 rounded transition duration-300'>
            Sign In
          </button>
        </div>
      </div>
    </header>
  );
}
