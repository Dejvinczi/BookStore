interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  fullWidth?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  fullWidth = false,
  className = "",
  ...props
}) => {
  return (
    <button
      className={`py-2 font-semibold rounded-md bg-accent text-primary hover:bg-secondary hover:text-accent focus:ring-4 focus:ring-primary ${fullWidth ? "w-full" : ""} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};
