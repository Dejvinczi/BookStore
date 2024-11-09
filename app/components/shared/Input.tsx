export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

const Input = ({ label, id, className = '', error, disabled, ...props }: InputProps) => {
  return (
    <div className="flex flex-col gap-1">
      {label && (
        <label htmlFor={id} className={`text-xl font-bold ${disabled ? 'text-gray-600' : 'text-light'}`}>
          {label}
        </label>
      )}
      <input
        id={id}
        disabled={disabled}
        className={`
          w-full px-3 py-2 rounded-md
          ${disabled ? 'bg-gray-600 text-gray-100 cursor-not-allowed' : 'bg-secondary focus:ring-4 focus:ring-accent'}
          ${error ? 'border-red-500' : ''}
          ${error && disabled ? 'border-red-300' : ''}
          placeholder:text-gray-400
          transition-colors
          ${className}
        `}
        {...props}
      />
      {error && <p className={`text-sm ${disabled ? 'text-red-300' : 'text-red-500'}`}>{error}</p>}
    </div>
  );
};

export default Input;
