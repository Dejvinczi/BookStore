export interface FormProps extends React.FormHTMLAttributes<HTMLFormElement> {
  title: string;
}

const Form = ({ title, children, className = '', ...props }: FormProps) => {
  return (
    <div className="flex items-center justify-center h-full">
      <div className="w-full max-w-md p-8 bg-primary rounded-lg shadow-lg">
        <h2 className="text-light text-3xl font-bold mb-6 text-center">{title}</h2>
        <form className={`space-y-4 ${className}`} {...props}>
          {children}
        </form>
      </div>
    </div>
  );
};

export default Form;
