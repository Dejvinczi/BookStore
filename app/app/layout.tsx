import Footer from '@/components/Footer';
import Header from '@/components/Header';
import { AuthProvider } from '@/contexts/AuthContext';
import '@/styles/globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'BookStore',
  description: 'Your favorite online BookStore',
};

interface RootLayoutProps {
  children: React.ReactNode;
}

const RootLayout = ({ children }: RootLayoutProps) => {
  return (
    <html lang="en">
      <body className="flex flex-col flex-1 min-h-screen max-h-screen bg-secondary text-light">
        <AuthProvider>
          <Header />
          <main className="flex flex-col flex-1 px-6 py-6">{children}</main>
          <Footer />
        </AuthProvider>
      </body>
    </html>
  );
};

export default RootLayout;
