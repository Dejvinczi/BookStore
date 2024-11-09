import Input from '@/components/shared/Input';
import React, { useState } from 'react';

export interface BookFilters {
  title: string;
  ordering: string;
  publicationDateAfter: string;
  publicationDateBefore: string;
}

export interface BookFiltersProps {
  onFiltersChange: (filters: BookFilters) => void;
}

const BookFilters = ({ onFiltersChange }: BookFiltersProps) => {
  const [filters, setFilters] = useState<BookFilters>({
    title: '',
    ordering: 'title',
    publicationDateAfter: '',
    publicationDateBefore: '',
  });

  const handleChange = (name: keyof BookFilters) => (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const newFilters = {
      ...filters,
      [name]: e.target.value,
    };
    setFilters(newFilters);
    onFiltersChange(newFilters);
  };

  return (
    <div className="w-fit mx-auto mb-4 border border-accent rounded-md bg-primary">
      <div className="flex justify-center gap-2 p-2">
        <Input
          id="title"
          type="text"
          placeholder="Search by title..."
          value={filters.title}
          onChange={handleChange('title')}
          className="w-80"
        />

        <select
          value={filters.ordering}
          onChange={handleChange('ordering')}
          className="w-60 px-3 py-2 rounded-md bg-secondary focus:ring-4 text-light focus:ring-accent appearance-none cursor-pointer"
        >
          <option value="title">Title (A-Z)</option>
          <option value="-title">Title (Z-A)</option>
          <option value="publication_date">Publication Date (Oldest)</option>
          <option value="-publication_date">Publication Date (Newest)</option>
        </select>

        <Input
          id="publishedAfter"
          type="date"
          value={filters.publicationDateAfter}
          onChange={handleChange('publicationDateAfter')}
          placeholder="mm/dd/yyyy"
          className="w-60"
        />

        <Input
          id="publishedBefore"
          type="date"
          value={filters.publicationDateBefore}
          onChange={handleChange('publicationDateBefore')}
          placeholder="mm/dd/yyyy"
          className="w-60 "
        />
      </div>
    </div>
  );
};

export default BookFilters;
