import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { AppRouterCacheProvider } from '@mui/material-nextjs/v14-appRouter';
import { ThemeProvider } from '@mui/material/styles';
import { Box, CssBaseline } from '@mui/material';
import Header from '@/src/app/_components/Header';
import Footer from '@/src/app/_components/Footer';
import { theme } from '@/src/app/theme';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
    title: 'BookStore',
    description: 'BookStore - The best book store in the world',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
    return (
        <html style={{ height: '100vh' }}>
            <body style={{ height: '100vh' }}>
                <AppRouterCacheProvider>
                    <ThemeProvider theme={theme}>
                        <CssBaseline />
                        <Header />
                        <Box component="main" sx={{ height: '85vh' }}>
                            {children}
                        </Box>
                        <Footer />
                    </ThemeProvider>
                </AppRouterCacheProvider>
            </body>
        </html>
    );
}
