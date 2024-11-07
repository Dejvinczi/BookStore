"use client";

import { useAuth } from "@/hooks/useAuth";
import {
  faBox,
  faRightFromBracket,
  faRightToBracket,
  faShoppingCart,
  faUserPlus,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Image from "next/image";
import Link from "next/link";

export default function Header() {
  const { user, logout } = useAuth();

  return (
    <header className='bg-primary'>
      <nav className='flex py-2 px-2'>
        <div className='container flex items-center justify-start'>
          <Link
            href='/'
            className='flex items-center gap-1 text-2xl font-bold hover:text-accent'
          >
            <Image
              src='/android-chrome-512x512.png'
              alt='Logo'
              width={22}
              height={22}
            />
            BookStore
          </Link>
        </div>

        <div className='container flex items-center justify-center gap-2'>
          <Link
            href='/books'
            className='px-2 py-2 rounded font-bold text-accent hover:bg-secondary'
          >
            BOOKS
          </Link>
        </div>

        <div className='container flex items-center justify-end gap-2'>
          {user ? (
            <>
              <Link
                href='/cart'
                className='px-2 py-2 rounded font-bold text-accent hover:bg-secondary'
              >
                <FontAwesomeIcon icon={faShoppingCart} />
              </Link>
              <Link
                href='/orders'
                className='px-2 py-2 rounded font-bold text-accent hover:bg-secondary'
              >
                <FontAwesomeIcon icon={faBox} />
              </Link>
              <button
                onClick={logout}
                className='px-2 py-2 rounded font-bold text-accent hover:bg-secondary'
              >
                <FontAwesomeIcon icon={faRightFromBracket} />
              </button>
            </>
          ) : (
            <>
              <Link
                href='/register'
                className='px-2 py-2 rounded font-bold text-accent hover:bg-secondary'
              >
                <FontAwesomeIcon icon={faUserPlus} />
              </Link>
              <Link
                href='/login'
                className='px-2 py-2 rounded font-bold text-accent hover:bg-secondary'
              >
                <FontAwesomeIcon icon={faRightToBracket} />
              </Link>
            </>
          )}
        </div>
      </nav>
    </header>
  );
}
