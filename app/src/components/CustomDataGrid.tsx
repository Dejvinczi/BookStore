import React from 'react';
import { DataGrid, GridColDef, GridRowsProp } from '@mui/x-data-grid';

interface CustomDataGridProps {
    columns: GridColDef[];
    rows: GridRowsProp;
}

const CustomDataGrid: React.FC<CustomDataGridProps> = ({ columns, rows }) => {
    return (
        <div style={{ height: '100%', width: '100%' }}>
            <DataGrid columns={columns} rows={rows} />
        </div>
    );
};

export default CustomDataGrid;
