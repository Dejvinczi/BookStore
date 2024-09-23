import Image from "next/image";
import Link from "next/link";

export default function Header() {
  return (
    <header className='py-4 px-4 bg-cream-50 shadow-md'>
      <div className='container mx-auto flex flex-col sm:flex-row items-center justify-between'>
        <Link href='/' className='flex items-center mb-4 sm:mb-0'>
          <Image
            src='/android-chrome-512x512.png'
            alt='Logo'
            width={26}
            height={26}
            className='mr-2'
          />
          <h1 className='text-2xl font-bold text-azure-700'>BookStore</h1>
        </Link>

        <nav className='flex space-x-4 sm:space-x-8 mb-4 sm:mb-0'>
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

        <button className='bg-azure-500 hover:bg-azure-700 text-white font-bold py-2 px-4 rounded transition duration-300'>
          Sign In
        </button>
      </div>
    </header>
  );
}
