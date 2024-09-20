export default function Footer() {
  const currentYear: number = new Date().getFullYear();

  return (
    <footer className='py-4 px-4 bg-cream-50'>
      <div className='container mx-auto text-center'>
        <p className='text-stone-600'>
          &copy; {currentYear} BookStore. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
