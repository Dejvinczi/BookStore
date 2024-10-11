interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
}

export const Input: React.FC<InputProps> = ({
  label,
  id,
  className = "",
  error,
  ...props
}) => {
  return (
    <div>
      <label htmlFor={id} className='sr-only'>
        {label}
      </label>
      <input
        id={id}
        className={`w-full px-3 py-2 rounded-md bg-secondary placeholder-gray-400 focus:ring-4 focus:ring-accent ${error ? "border-red-500" : ""} ${className}`}
        {...props}
      />
      {error && <p className='mt-1 text-sm text-red-500'>{error}</p>}
    </div>
  );
};
