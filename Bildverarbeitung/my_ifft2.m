function [A] = my_ifft2(ftA)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
A = fftshift(ifft2(fftshift(ftA)));
end