"use client";

import { useAuth } from "@/hooks/useAuth";
import Image from "next/image";
import Link from "next/link";

export default function Header() {
  const { user, logout } = useAuth();

  return (
    <header className='bg-primary text-text shadow-md'>
      <nav className='container mx-auto px-4 py-4'>
        <div className='flex flex-wrap justify-between items-center'>
          <Link
            href='/'
            className='flex items-center text-2xl font-bold hover:text-accent'
          >
            <Image
              src='/android-chrome-512x512.png'
              alt='Logo'
              width={22}
              height={22}
              className='mr-1'
            />
            BookStore
          </Link>

          <div className='flex items-center space-x-2'>
            <Link
              href='/books'
              className='text-accent hover:bg-secondary hover:text-accent px-4 py-1 rounded transition-colors font-bold'
            >
              Books
            </Link>
          </div>

          <div className='flex items-center space-x-2'>
            {user ? (
              <>
                <Link
                  href='/cart'
                  className='text-accent hover:bg-secondary hover:text-accent px-4 py-1 rounded transition-colors font-bold'
                >
                  Cart
                </Link>
                <button
                  onClick={logout}
                  className='text-accent hover:bg-secondary hover:text-accent px-4 py-1 rounded transition-colors font-bold'
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <Link
                  href='/login'
                  className='text-accent hover:bg-secondary hover:text-accent px-4 py-1 rounded transition-colors font-bold'
                >
                  Login
                </Link>
                <Link
                  href='/register'
                  className='text-accent hover:bg-secondary hover:text-accent px-4 py-1 rounded transition-colors font-bold'
                >
                  Register
                </Link>
              </>
            )}
          </div>
        </div>
      </nav>
    </header>
  );
}
