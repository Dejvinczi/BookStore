import { GridColDef } from '@mui/x-data-grid';
import CustomDataGrid from '@/src/components/CustomDataGrid';

interface Author {
    id: number;
    title: string;
    author: string;
    publishedDate: string;
}

const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'first_name', headerName: 'First Name', flex: 1 },
    { field: 'last_name', headerName: 'Last Name', flex: 1 },
    { field: 'date_of_birth', headerName: 'Date of Birth', flex: 1 },
];

const fetchAuthors = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/authors/`, {
        cache: 'no-store',
    });
    if (!res.ok) {
        throw new Error('Failed to fetch data');
    }
    return res.json();
};

const AuthorsPage = async () => {
    const authors = await fetchAuthors();
    return (
        <div style={{ height: '100%', width: '100%' }}>
            <CustomDataGrid columns={columns} rows={authors.results} />
        </div>
    );
};

export default AuthorsPage;
