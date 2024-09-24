"use client";

import React, { createContext, useState, useEffect, useCallback } from "react";
import { getToken, storeToken, removeTokens, decodeToken } from "@/utils/token";
import { User } from "@/types/user";
import api from "@/utils/axios";

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  register: (
    email: string,
    username: string,
    password: string
  ) => Promise<void>;
}

export const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const checkLoginStatus = useCallback(async () => {
    setLoading(true);
    const access = getToken("access");
    if (access) {
      const { user_id } = decodeToken(access);
      setUser({ id: user_id });
    } else {
      await refresh();
    }
    setLoading(false);
  }, []);

  useEffect(() => {
    checkLoginStatus();
  }, [checkLoginStatus]);

  const login = async (username: string, password: string) => {
    setLoading(true);
    try {
      const response = await api.post("/login", { username, password });
      storeToken("access", response.data.access);
      storeToken("refresh", response.data.refresh);

      const { user_id } = decodeToken(response.data.access);
      setUser({ id: user_id });
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    setLoading(true);
    const refresh = getToken("refresh");
    if (refresh) {
      try {
        await api.post("/logout", { refresh });
      } catch (error) {
        console.error("Logout failed", error);
      } finally {
        setLoading(false);
      }
    }
    removeTokens();
    setUser(null);
  };

  const refresh = async () => {
    setLoading(true);
    const refresh = getToken("refresh");
    if (refresh) {
      try {
        const response = await api.post("/login/refresh", { refresh });
        storeToken("access", response.data.access);
        storeToken("refresh", response.data.refresh);
      } catch (error) {
        console.error("Refresh failed", error);
      } finally {
        setLoading(false);
      }
    }
  };

  const register = async (
    email: string,
    username: string,
    password: string
  ) => {
    setLoading(true);
    try {
      await api.post("/register", { email, username, password });
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout, register }}>
      {children}
    </AuthContext.Provider>
  );
}
