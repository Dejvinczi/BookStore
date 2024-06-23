import { GridColDef } from '@mui/x-data-grid';
import CustomDataGrid from '@/src/components/CustomDataGrid';

interface Book {
    id: number;
    title: string;
    author: string;
    publishedDate: string;
}

const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'title', headerName: 'Title', flex: 1 },
    { field: 'authors', headerName: 'Authors', flex: 1 },
    { field: 'genres', headerName: 'Genres', flex: 1 },
    { field: 'publication_date', headerName: 'Publication Date', flex: 1 },
];

const fetchBooks = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/books/`, {
        cache: 'no-store',
    });
    if (!res.ok) {
        throw new Error('Failed to fetch data');
    }
    return res.json();
};

const BooksPage = async () => {
    const books = await fetchBooks();
    return (
        <div style={{ height: '100%', width: '100%' }}>
            <CustomDataGrid columns={columns} rows={books.results} />
        </div>
    );
};

export default BooksPage;
