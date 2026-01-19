# SQL blind injections

1. Visit the front page of the shop, and use Burp Suite to intercept and modify the request containing the TrackingId cookie. For simplicity, let's say the original value of the cookie is TrackingId=xyz.
2. Modify the TrackingId cookie, changing it to:
TrackingId=xyz' AND '1'='1
    
    Verify that the Welcome back message appears in the response.
    
3. Now change it to:
TrackingId=xyz' AND '1'='2
    
    Verify that the Welcome back message does not appear in the response. This demonstrates how you can test a single boolean condition and infer the result.
    
4. Now change it to:
TrackingId=xyz' AND (SELECT 'a' FROM users LIMIT 1)='a
5. Verify that the condition is true, confirming that there is a table called users.
6. Now change it to:
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator')='a
7. Verify that the condition is true, confirming that there is a user called administrator.
8. The next step is to determine how many characters are in the password of the administrator user. To do this, change the value to:
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a
9. This condition should be true, confirming that the password is greater than 1 character in length.
10. Send a series of follow-up values to test different password lengths. Send:
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>2)='a
11. Then send:
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>3)='a , and so on. You can do this manually using Burp Repeater, since the length is likely to be short. When the condition stops being true (i.e. when the Welcome back message disappears), you have determined the length of the password, which is in fact 20 characters long.
After determining the length of the password, the next step is to test the character at each position to determine its value. This involves a much larger number of requests, so you need to use Burp Intruder. Send the request you are working on to Burp Intruder, using the context menu.
12. In Burp Intruder, change the value of the cookie to:
`TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a` . This uses the SUBSTRING() function to extract a single character from the password, and test it against a specific value. Our attack will cycle through each position and possible value, testing each one in turn.
13. Place payload position markers around the final a character in the cookie value. To do this, select just the a, and click the Add § button. You should then see the following as the cookie value (note the payload position markers):
`TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='§a§`
To test the character at each position, you'll need to send suitable payloads in the payload position that you've defined. You can assume that the password contains only lowercase alphanumeric characters. In the Payloads side panel, check that Simple list is selected. Then check the add list, if you don´t have pro try to download a txt that have the alphanumeric lowercase alphabet. If not, add it manually.
14. To be able to tell when the correct character was submitted, you'll need to grep each response for the expression that appeared when you started in `' AND '1' = '1`. To do this, click on the Settings tab to open the Settings side panel. In the Grep - Match section, clear existing entries in the list, then add the value that you encauntered.
    
    *If you want to load more payloads, such as changing the position in the password from, for example, `SUBSTRING(password 1, 1)` the first position to automatically the second one, `SUBSTRING(password 2, 1)` you will need to add a sacond payload and change the attack type to cluster bomb:
    

## Cluster bomb

- This allows you to try to bruteforce with several payloads
- It is slow but steady
- You will need to position the payloads correctly
- In the payloads configuration change the position to select wich payload will you be modifying
- Select the correct list for each of the payloads
1. Launch the attack by clicking the Start attack button.
Review the attack results to find the value of the character at the first position. You should see a column in the results called <message that you wanted to grep>. One of the rows should have a tick or a 1 in this column. The payload showing for that row is the value of the character at the <x> position.
    - To simplify your life and not to run through the list looking to that tick, simply click on the column that has your message
2. Now you have it!