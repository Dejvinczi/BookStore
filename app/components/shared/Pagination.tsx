interface PaginationProps {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
  hasNext: boolean;
  hasPrevious: boolean;
}

const Pagination = ({ currentPage, totalPages, onPageChange, hasNext, hasPrevious }: PaginationProps) => {
  const getPageNumbers = () => {
    const pages = [];
    const showEllipsisStart = currentPage > 3;
    const showEllipsisEnd = currentPage < totalPages - 2;

    if (totalPages <= 7) {
      return Array.from({ length: totalPages }, (_, i) => i + 1);
    }

    pages.push(1);

    if (showEllipsisStart) {
      pages.push('ellipsis');
    }

    for (let i = Math.max(2, currentPage - 1); i <= Math.min(currentPage + 1, totalPages - 1); i++) {
      pages.push(i);
    }

    if (showEllipsisEnd) {
      pages.push('ellipsis');
    }

    if (totalPages > 1) {
      pages.push(totalPages);
    }

    return pages;
  };

  return (
    <div className="flex justify-center items-center gap-2 mt-8">
      <button
        onClick={() => onPageChange(currentPage - 1)}
        disabled={!hasPrevious}
        className="bg-primary border-2 border-accent text-accent hover:bg-secondary disabled:opacity-50 disabled:hover:bg-primary font-bold py-2 px-4 rounded-lg transition duration-300"
      >
        Previous
      </button>

      <div className="flex gap-2">
        {getPageNumbers().map((page) => (
          <>
            {page === 'ellipsis' ? (
              <span className="text-accent font-bold px-3 py-2">...</span>
            ) : (
              <button
                onClick={() => onPageChange(Number(page))}
                className={`
                  w-10 h-10 rounded-lg font-bold transition duration-300
                  ${
                    currentPage === page
                      ? 'bg-accent text-primary border-2 border-accent'
                      : 'bg-primary border-2 border-accent text-accent hover:bg-secondary'
                  }
                `}
              >
                {page}
              </button>
            )}
          </>
        ))}
      </div>

      <button
        onClick={() => onPageChange(currentPage + 1)}
        disabled={!hasNext}
        className="bg-primary border-2 border-accent text-accent hover:bg-secondary disabled:opacity-50 disabled:hover:bg-primary font-bold py-2 px-4 rounded-lg transition duration-300"
      >
        Next
      </button>
    </div>
  );
};

export default Pagination;
