import { Avatar, AvatarsGroup, Box } from '@mantine/core';
// import UserAvatar from './UserAvatar';

const UsersRow = ({ users }) => {
  return (
    <Box>
      <AvatarsGroup>
        {users.map((user, i) => (
          <Avatar key={i} radius="xl" color="grape">
            {user.charAt(0).toUpperCase()}
          </Avatar>
        ))}
      </AvatarsGroup>
    </Box>
  );
};

export default UsersRow;