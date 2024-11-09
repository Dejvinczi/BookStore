'use client';

import Button from '@/components/shared/Button';
import Form from '@/components/shared/Form';
import Input from '@/components/shared/Input';
import { useAuth } from '@/hooks/useAuth';
import { ApiError } from '@/types/api';
import { useRouter } from 'next/navigation';
import { FormEvent, useState } from 'react';

interface FormErrors {
  username?: string;
  password?: string;
  general?: string;
}

const LoginPage = () => {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [errors, setErrors] = useState<FormErrors>({});
  const router = useRouter();
  const { login } = useAuth();

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setErrors({});
    try {
      await login(username, password);
      router.push('/');
    } catch (error) {
      const err = error as ApiError;
      if (err.response) {
        if (err.response.status === 400) {
          if (err.response.data.detail) {
            setErrors({ general: err.response.data.detail });
          } else {
            setErrors(err.response.data as FormErrors);
          }
        } else if (err.response.status === 401) {
          setErrors({ general: 'Incorrect username or password.' });
        }
      } else {
        setErrors({
          general: 'An unexpected error occurred. Please try again.',
        });
      }
      console.error('Login failed', error);
    }
  };

  return (
    <Form title="Sign in to your account" onSubmit={handleSubmit}>
      <Input
        id="username"
        name="username"
        type="text"
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
        autoComplete="current-password"
        required
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        error={errors.password}
      />
      {errors.general && <p className="text-red-500 text-sm mb-4">{errors.general}</p>}
      <Button type="submit" fullWidth>
        Sign in
      </Button>
    </Form>
  );
};

export default LoginPage;
