import { GridColDef } from '@mui/x-data-grid';
import CustomDataGrid from '@/src/components/CustomDataGrid';

interface Genre {
    id: number;
    name: string;
}

const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'name', headerName: 'Name', flex: 1 },
];

const fetchGenres = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/genres/`, {
        cache: 'no-store',
    });
    if (!res.ok) {
        throw new Error('Failed to fetch data');
    }
    return res.json();
};

const GenresPage = async () => {
    const genres = await fetchGenres();
    return (
        <div style={{ height: '100%', width: '100%' }}>
            <CustomDataGrid columns={columns} rows={genres.results} />
        </div>
    );
};

export default GenresPage;
