interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  fullWidth?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  fullWidth = false,
  className = "",
  disabled,
  ...props
}) => {
  return (
    <button
      disabled={disabled}
      className={`
        py-2 px-4
        font-semibold
        rounded-md
        transition-colors
        ${fullWidth ? "w-full" : ""}
        ${
          disabled
            ? "bg-gray-600 text-gray-400 cursor-not-allowed"
            : "bg-accent text-primary hover:bg-secondary hover:text-accent focus:ring-4 focus:ring-primary"
        }
        ${className}
      `}
      {...props}
    >
      <span className='flex items-center justify-center gap-2'>{children}</span>
    </button>
  );
};
