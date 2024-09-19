import Link from "next/link";

export default function Navigation() {
  return (
    <nav>
      <ul>
        <li>
          <Link href='/books'>Books</Link>
        </li>
      </ul>
    </nav>
  );
}
