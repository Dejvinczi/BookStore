export default function Footer() {
  const currentYear: number = new Date().getFullYear();

  return (
    <footer className='bg-primary py-4'>
      <div className='container mx-auto px-4 text-center text-light '>
        <p>&copy; {currentYear} BookStore. All rights reserved.</p>
      </div>
    </footer>
  );
}
