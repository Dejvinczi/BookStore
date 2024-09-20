import type { Metadata } from "next";
import Header from "@components/Header";
import Footer from "@components/Footer";
import "@styles/globals.css";

export const metadata: Metadata = {
  title: "BookStore",
  description: "Your favorite bookstore",
  icons: {
    icon: "/favicon.ico",
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang='en'>
      <body className='flex min-h-screen flex-col bg-cream-50 text-stone-700'>
        <Header />
        <main className='container mx-auto flex-grow px-4 py-8'>
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
