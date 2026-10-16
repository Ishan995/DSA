class Solution:
    def simplifyPath(self, path: str) -> str:
        components=path.split('/')
        st=[]
        for part in components:
            if part=='..':
                if st: st.pop()
            elif part not in ['','.']:
                st.append(part)
        return '/' + '/'.join(st)
            