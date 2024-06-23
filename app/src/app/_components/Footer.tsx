import React from 'react';
import { Box, Typography } from '@mui/material';

const Footer = () => {
    return (
        <Box component="footer" sx={{ py: 1, textAlign: 'center' }}>
            <Typography variant="body2" color="textSecondary">
                &copy; 2024 BookStore. All rights reserved. License information.
            </Typography>
        </Box>
    );
};

export default Footer;
