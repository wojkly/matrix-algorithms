function []=gen_mat(a,b,c,d,filename)


  m = massmatrix(a,b,c,d)
  A = full(m)

  fid=fopen(filename,'w+');
  for i=1:size(A, 1)
    for j=1: (size(A, 2) - 1)
      fprintf(fid, '%.15f,', A(i,j));
    end
    fprintf(fid, '%.15f\n', A(i,size(A, 2)));
  end
  fclose(fid);

end