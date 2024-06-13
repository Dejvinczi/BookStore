'use client';
import React, { useState } from 'react';
import Link from 'next/link';
import { AppBar, Toolbar, Typography, IconButton, Button, Box } from '@mui/material';
import { Menu, AccountCircle } from '@mui/icons-material';
import LockOpenIcon from '@mui/icons-material/LockOpen';
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import Sidebar from '@/src/app/_components/SideBar';

const Header = () => {
    const [sidebarOpen, setSidebarOpen] = useState(false);

    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };
    return (
        <Box component={'header'}>
            <AppBar position="static">
                <Sidebar isOpen={sidebarOpen} onClose={toggleSidebar} />
                <Toolbar>
                    <IconButton edge="start" onClick={toggleSidebar}>
                        <Menu />
                    </IconButton>
                    <Typography variant="h5" component="div" sx={{ flexGrow: 1 }}>
                        BookStore
                    </Typography>
                    <Box>
                        <Link href="/profile" passHref>
                            <Button startIcon={<AccountCircle />}>Profile</Button>
                        </Link>
                        <Link href="/signin" passHref>
                            <Button startIcon={<LockOpenIcon />}>Sign In</Button>
                        </Link>
                        <Link href="/signup" passHref>
                            <Button startIcon={<PersonAddIcon />}>Sign Up</Button>
                        </Link>
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>
    );
};

export default Header;
