conn = sqlite('test.db');
query = 'SELECT * FROM test_table;';
table = fetch(conn, query);
close(conn);

ts_strs = table.timestamp;
tic;
len = numel(ts_strs);
ts = NaT(len, 1);
for ii = 1:len
    if mod(ii, 1000) == 0
        disp(ii) 
    end
    % Convert each string to a datetime object
    ts(ii) = datetime(ts_strs{ii});
end
toc