import React from 'react';
import { useRouter } from 'next/navigation';
import { Drawer, List, ListItemButton, ListItemText, ListItemIcon, Divider } from '@mui/material';
import MenuBookIcon from '@mui/icons-material/MenuBook';
import AutoAwesomeMotionIcon from '@mui/icons-material/AutoAwesomeMotion';
import GroupsIcon from '@mui/icons-material/Groups';
import HomeIcon from '@mui/icons-material/Home';

interface SidebarProps {
    isOpen: boolean;
    onClose: () => void;
}

const Sidebar = ({ isOpen, onClose }: SidebarProps) => {
    const router = useRouter();

    const handleNavigation = (path: string) => {
        router.push(path);
        onClose();
    };

    return (
        <Drawer open={isOpen} onClose={onClose} anchor="left">
            <List>
                <ListItemButton onClick={() => handleNavigation('/')}>
                    <ListItemIcon>
                        <HomeIcon />
                    </ListItemIcon>
                    <ListItemText primary="Home" />
                </ListItemButton>
                <Divider />
                <ListItemButton onClick={() => handleNavigation('/books')}>
                    <ListItemIcon>
                        <MenuBookIcon />
                    </ListItemIcon>
                    <ListItemText primary="Books" />
                </ListItemButton>
                <ListItemButton onClick={() => handleNavigation('/genres')}>
                    <ListItemIcon>
                        <AutoAwesomeMotionIcon />
                    </ListItemIcon>
                    <ListItemText primary="Genres" />
                </ListItemButton>
                <ListItemButton onClick={() => handleNavigation('/authors')}>
                    <ListItemIcon>
                        <GroupsIcon />
                    </ListItemIcon>
                    <ListItemText primary="Authors" />
                </ListItemButton>
            </List>
        </Drawer>
    );
};

export default Sidebar;
