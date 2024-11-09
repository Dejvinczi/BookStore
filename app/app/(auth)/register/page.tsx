'use client';

import Button from '@/components/shared/Button';
import Form from '@/components/shared/Form';
import Input from '@/components/shared/Input';
import { useAuth } from '@/hooks/useAuth';
import { ApiError } from '@/types/api';
import { useRouter } from 'next/navigation';
import { FormEvent, useState } from 'react';

interface FormErrors {
  email?: string;
  username?: string;
  password?: string;
  confirmPassword?: string;
  general?: string;
}

const RegisterPage = () => {
  const [email, setEmail] = useState<string>('');
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [confirmPassword, setConfirmPassword] = useState<string>('');
  const [errors, setErrors] = useState<FormErrors>({});
  const router = useRouter();
  const { register } = useAuth();

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setErrors({});
    if (password !== confirmPassword) {
      const errorMsg = "Passwords don't match.";
      setErrors({ password: errorMsg, confirmPassword: errorMsg });
      return;
    }
    try {
      await register(email, username, password);
      router.push('/login');
    } catch (error) {
      const err = error as ApiError;
      if (err.response && err.response.status === 400) {
        if (err.response.data.detail) {
          setErrors({ general: err.response.data.detail });
        } else {
          setErrors(err.response.data as FormErrors);
        }
      } else {
        setErrors({
          general: 'An unexpected error occurred. Please try again.',
        });
        console.error('Register failed', error);
      }
    }
  };

  return (
    <Form title="Create your account" onSubmit={handleSubmit}>
      <Input
        id="email-address"
        name="email"
        type="email"
        autoComplete="email"
        required
        placeholder="Email address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        error={errors.email}
      />
      <Input
        id="username"
        name="username"
        type="username"
        autoComplete="username"
        required
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        error={errors.username}
      />
      <Input
        id="password"
        name="password"
        type="password"
        autoComplete="new-password"
        required
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        error={errors.password}
      />
      <Input
        id="confirm-password"
        name="confirm-password"
        type="password"
        autoComplete="new-password"
        required
        placeholder="Confirm Password"
        value={confirmPassword}
        onChange={(e) => setConfirmPassword(e.target.value)}
        error={errors.confirmPassword}
      />
      {errors.general && <p className="text-red-500 text-sm mb-4">{errors.general}</p>}
      <Button type="submit" fullWidth>
        Register
      </Button>
    </Form>
  );
};

export default RegisterPage;
