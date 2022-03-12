/* eslint-disable camelcase */
import makeRequest, { makeNonJsonRequest } from './request';

export const fromApiFiles = ({
  query_id,
  last_modified,
  created_at,
  ...rest
}) => ({
  id: query_id,
  lastModified: last_modified,
  createdAt: created_at,
  ...rest,
});
export const toApiFiles = ({ id, lastModified, createdAt, ...rest }) => ({
  query_id: id,
  last_modified: lastModified,
  created_at: createdAt,
  ...rest,
});

export const getFiles = async (projectId) => {
  const response = await makeRequest(`/projects/${projectId}/files`);
  const apiFiles = await response.json();
  return apiFiles.map(fromApiFiles);
};

export const uploadFile = (projectId, file) => {
  const formdata = new FormData();
  formdata.append('name', file.name);
  formdata.append('project', projectId);
  formdata.append('file', file, file.name);
  formdata.append('mimetype', file.type || 'application/octet-stream');

  return makeNonJsonRequest(`/projects/${projectId}/files`, {
    method: 'POST',
    body: formdata,
  });
};

export const deleteFile = async (projectId, fileId) => {
  const response = makeRequest(`/projects/${projectId}/files/${fileId}`, {
    method: 'DELETE',
  });
  return response.status === 204;
};
