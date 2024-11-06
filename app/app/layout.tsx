import Footer from "@/components/Footer";
import Header from "@/components/Header";
import { AuthProvider } from "@/contexts/AuthContext";
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
      <body className='flex flex-col min-h-screen bg-secondary text-light'>
        <AuthProvider>
          <Header />
          <main className='flex-1 flex flex-col px-6 py-6'>{children}</main>
          <Footer />
        </AuthProvider>
      </body>
    </html>
  );
}
