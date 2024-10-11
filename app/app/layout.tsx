import { AuthProvider } from "@/contexts/AuthContext";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import "@/styles/globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "BookStore",
  description: "Your favorite online bookstore",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang='en'>
      <body className='bg-secondary text-light flex flex-col min-h-screen'>
        <AuthProvider>
          <Header />
          <main className='flex-grow container mx-auto px-4 py-8'>
            {children}
          </main>
          <Footer />
        </AuthProvider>
      </body>
    </html>
  );
}
