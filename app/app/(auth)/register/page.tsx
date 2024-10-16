"use client";

import { useState, FormEvent } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";
import { Form } from "@/components/shared/Form";
import { Input } from "@/components/shared/Input";
import { Button } from "@/components/shared/Button";

interface FormErrors {
  email?: string;
  username?: string;
  password?: string;
  confirmPassword?: string;
  general?: string;
}

export default function RegisterPage() {
  const [email, setEmail] = useState<string>("");
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [confirmPassword, setConfirmPassword] = useState<string>("");
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
      router.push("/login");
    } catch (error: any) {
      if (error.response && error.response.status === 400) {
        if (error.response.data.detail) {
          setErrors({ general: error.response.data.detail });
        } else {
          setErrors(error.response.data);
        }
      } else {
        setErrors({
          general: "An unexpected error occurred. Please try again.",
        });
        console.error("Register failed", error);
      }
    }
  };

  return (
    <Form title='Create your account' onSubmit={handleSubmit}>
      <Input
        label='Email address'
        id='email-address'
        name='email'
        type='email'
        autoComplete='email'
        required
        placeholder='Email address'
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        error={errors.email}
      />
      <Input
        label='Username'
        id='username'
        name='username'
        type='username'
        autoComplete='username'
        required
        placeholder='Username'
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        error={errors.username}
      />
      <Input
        label='Password'
        id='password'
        name='password'
        type='password'
        autoComplete='new-password'
        required
        placeholder='Password'
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        error={errors.password}
      />
      <Input
        label='Confirm Password'
        id='confirm-password'
        name='confirm-password'
        type='password'
        autoComplete='new-password'
        required
        placeholder='Confirm Password'
        value={confirmPassword}
        onChange={(e) => setConfirmPassword(e.target.value)}
        error={errors.confirmPassword}
      />
      {errors.general && (
        <p className='text-red-500 text-sm mb-4'>{errors.general}</p>
      )}
      <Button type='submit' fullWidth>
        Register
      </Button>
    </Form>
  );
}
